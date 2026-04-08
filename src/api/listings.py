from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import Optional

from src.database import get_db
from src.models.listing import Listing

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/listings", response_class=HTMLResponse)
def list_listings(
    request: Request,
    business_type: Optional[str] = None,
    seller_financing: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Listing).filter(Listing.is_active == True)
    if business_type:
        query = query.filter(Listing.business_type == business_type)
    if seller_financing:
        query = query.filter(Listing.seller_financing_available == True)
    listings = query.order_by(Listing.created_at.desc()).all()
    return templates.TemplateResponse(
        "listings.html",
        {"request": request, "listings": listings, "business_type": business_type, "seller_financing": seller_financing},
    )


@router.get("/listings/new", response_class=HTMLResponse)
def new_listing_form(request: Request):
    from src.models.listing import BusinessType
    return templates.TemplateResponse(
        "listing_form.html",
        {"request": request, "business_types": [bt.value for bt in BusinessType]},
    )


@router.post("/listings/new")
def create_listing(
    request: Request,
    title: str = Form(...),
    business_type: str = Form(...),
    location: str = Form(...),
    asking_price: float = Form(...),
    annual_revenue: Optional[float] = Form(None),
    annual_cash_flow: Optional[float] = Form(None),
    description: str = Form(...),
    seller_financing_available: bool = Form(False),
    sf_down_payment_pct: Optional[float] = Form(None),
    sf_interest_rate: Optional[float] = Form(None),
    sf_term_years: Optional[int] = Form(None),
    contact_name: str = Form(...),
    contact_email: str = Form(...),
    contact_phone: Optional[str] = Form(None),
    attorney_involved: bool = Form(False),
    db: Session = Depends(get_db),
):
    listing = Listing(
        title=title,
        business_type=business_type,
        location=location,
        asking_price=asking_price,
        annual_revenue=annual_revenue,
        annual_cash_flow=annual_cash_flow,
        description=description,
        seller_financing_available=seller_financing_available,
        sf_down_payment_pct=sf_down_payment_pct if seller_financing_available else None,
        sf_interest_rate=sf_interest_rate if seller_financing_available else None,
        sf_term_years=sf_term_years if seller_financing_available else None,
        contact_name=contact_name,
        contact_email=contact_email,
        contact_phone=contact_phone,
        attorney_involved=attorney_involved,
    )
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return RedirectResponse(url=f"/listings/{listing.id}", status_code=303)


@router.get("/listings/{listing_id}", response_class=HTMLResponse)
def view_listing(request: Request, listing_id: int, db: Session = Depends(get_db)):
    listing = db.query(Listing).filter(Listing.id == listing_id, Listing.is_active == True).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return templates.TemplateResponse("listing_detail.html", {"request": request, "listing": listing})
