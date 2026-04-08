from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")

FAQ_ITEMS = [
    {
        "category": "Buying a Business",
        "questions": [
            {
                "q": "What is due diligence and why is it important?",
                "a": (
                    "Due diligence is the investigation of a business before you commit to buying it. "
                    "It includes reviewing financial statements (typically 3 years), tax returns, leases, "
                    "contracts, employee agreements, and any pending litigation. In Pennsylvania, you should "
                    "also check for any state-level liens filed with the Pennsylvania Department of Revenue "
                    "and verify the business's standing with the Pennsylvania Department of State."
                ),
            },
            {
                "q": "Do I need an attorney to buy a business in Pennsylvania?",
                "a": (
                    "While not legally required, an attorney is strongly recommended. A Pennsylvania business "
                    "attorney will review and negotiate the Asset Purchase Agreement or Stock Purchase Agreement, "
                    "ensure proper UCC lien searches are conducted, handle the transfer of licenses, and verify "
                    "that no state tax obligations transfer to you unexpectedly. Many buyers also engage a CPA "
                    "to review the seller's financials independently."
                ),
            },
            {
                "q": "What's the difference between buying assets vs. buying stock?",
                "a": (
                    "In an asset purchase, you buy specific assets of the business (equipment, inventory, "
                    "goodwill, customer lists) and generally do not inherit the seller's liabilities. "
                    "In a stock purchase, you buy the seller's ownership shares and inherit all assets "
                    "AND liabilities. Asset purchases are more common for small businesses; most buyers "
                    "prefer them to avoid hidden liabilities. Pennsylvania does not impose a state transfer "
                    "tax on asset sales, though local realty transfer taxes apply if real estate is included."
                ),
            },
            {
                "q": "What licenses and permits do I need to transfer in Pennsylvania?",
                "a": (
                    "Licenses are generally not transferable — you must apply in your own name. Common licenses include: "
                    "Pennsylvania business registration (PA Department of State), sales tax license (PA Department of Revenue), "
                    "local business/occupancy permits from the municipality, and industry-specific licenses "
                    "(e.g., liquor license from the Pennsylvania Liquor Control Board, food service permit from the "
                    "PA Department of Agriculture). Allow 60–90 days for liquor license transfers."
                ),
            },
        ],
    },
    {
        "category": "Seller Financing",
        "questions": [
            {
                "q": "What is seller financing?",
                "a": (
                    "Seller financing (also called owner financing) is when the seller acts as the lender. "
                    "Instead of the buyer getting a bank loan for the full amount, the seller accepts a down "
                    "payment and the buyer makes monthly payments directly to the seller over an agreed term, "
                    "typically at a negotiated interest rate. It is common in small business transactions "
                    "and can make deals easier to close when bank financing is difficult to obtain."
                ),
            },
            {
                "q": "What are typical seller financing terms?",
                "a": (
                    "Terms vary, but common ranges are: Down payment 20–30% of the purchase price; "
                    "Interest rate 5–8% annually; Repayment term 3–7 years. The promissory note and "
                    "any collateral agreement should be drafted by an attorney and should specify what "
                    "happens in case of default."
                ),
            },
            {
                "q": "Is a seller financing agreement legally enforceable in Pennsylvania?",
                "a": (
                    "Yes. A properly drafted promissory note is legally enforceable under Pennsylvania law "
                    "(13 Pa.C.S. § 3101 et seq., the Pennsylvania version of the UCC). The seller may also "
                    "file a UCC-1 financing statement with the Pennsylvania Department of State to perfect "
                    "a security interest in the business assets, protecting their position if the buyer defaults."
                ),
            },
            {
                "q": "What happens if a buyer defaults on seller financing in Pennsylvania?",
                "a": (
                    "The seller can pursue remedies under the promissory note, which typically include "
                    "declaring the full balance due (acceleration clause), repossessing collateral secured "
                    "by a UCC filing, and filing a lawsuit for the outstanding balance. Pennsylvania courts "
                    "handle these as commercial contract disputes. Having an attorney draft the note with "
                    "clear default and remedy provisions is essential."
                ),
            },
        ],
    },
    {
        "category": "Selling a Business",
        "questions": [
            {
                "q": "How do I value my business?",
                "a": (
                    "The most common valuation method for small businesses is a multiple of Seller's "
                    "Discretionary Earnings (SDE) — typically 1.5x to 3x SDE depending on business type, "
                    "growth, industry, and transferability. A restaurant might sell at 1.5–2x SDE while "
                    "a profitable service business might reach 2.5–3x. An independent business broker or "
                    "a certified business valuator (CBV) can provide a formal valuation."
                ),
            },
            {
                "q": "What Pennsylvania taxes apply when I sell my business?",
                "a": (
                    "Pennsylvania imposes a flat 3.07% personal income tax on capital gains from business "
                    "sales for individuals, in addition to the federal capital gains tax. Pennsylvania does "
                    "not have a separate capital gains rate — gains are taxed as ordinary income at 3.07%. "
                    "Installment sales (seller financing) allow you to spread gain recognition over the "
                    "payment period, potentially smoothing your tax liability. Consult a CPA for your "
                    "specific situation."
                ),
            },
            {
                "q": "Do I need a non-compete agreement?",
                "a": (
                    "Buyers typically require sellers to sign a non-compete agreement to protect the goodwill "
                    "they're paying for. In Pennsylvania, non-competes are enforceable if they are reasonable "
                    "in scope, geographic area, and duration. Courts have generally upheld 2–3 year non-competes "
                    "within a defined geographic region. Overly broad non-competes may be modified or voided "
                    "by a Pennsylvania court."
                ),
            },
        ],
    },
    {
        "category": "Legal Teams & Closing",
        "questions": [
            {
                "q": "When should I involve an attorney in the process?",
                "a": (
                    "Ideally, engage an attorney before signing a Letter of Intent (LOI). The LOI may include "
                    "binding provisions such as exclusivity and confidentiality clauses. Your attorney should "
                    "also review the purchase agreement, any lease assignment, the bill of sale, and coordinate "
                    "with the other party's counsel to ensure a clean closing."
                ),
            },
            {
                "q": "What happens at closing?",
                "a": (
                    "At closing, both parties sign the Purchase Agreement, Bill of Sale, promissory note "
                    "(if seller financing), non-compete agreement, and any assignment of lease or contracts. "
                    "Funds are exchanged (often via escrow), and ownership transfers. In Pennsylvania, if "
                    "real property is included, the deed must be recorded with the county recorder of deeds "
                    "and realty transfer tax paid."
                ),
            },
        ],
    },
]


@router.get("/faq", response_class=HTMLResponse)
def faq_page(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request, "faq_items": FAQ_ITEMS})
