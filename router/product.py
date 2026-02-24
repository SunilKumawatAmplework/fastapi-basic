from fastapi import APIRouter, Depends, Header, Cookie, Form
from typing import Optional, List
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.data import getDB
from db import db_user
from typing import List
from fastapi.responses import Response, PlainTextResponse, HTMLResponse
from custom_log import debug_log


router = APIRouter(prefix="/product", tags=["products"])

products = ["watch", "phone", "laptop"]


@router.get("/all")
def get_all_product():
    debug_log("My", " Call to get all product")
    # return products
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.post("/new")
def create_product(name: str = Form(...)):
    products.append(name)
    return {"data": products}


@router.get("/withheader")
def get_product_with_header(
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None),
):
    if custom_header:
        response.headers["custom-response-header"] = ",".join(custom_header)
    return {"data": products, "cookie": test_cookie, "custom_header": custom_header}


@router.get("/{id}")
def get_product(id: int):
    if id > len(products):
        out = "Product not found"
        return PlainTextResponse(content=out, status_code=404, media_type="text/plain")
    product = products[id]
    # return Response(content=product, media_type="text/plain")
    out = f"""
     <head>
      <style>
       .product {{
        background-color: red;
        color: white;
       }}
      </style>
    </head>
    <div class="product">
      <h1>{product}</h1>
    </div>
  """
    return HTMLResponse(content=out, media_type="text/html")
