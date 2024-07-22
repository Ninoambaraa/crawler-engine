# Web Crawler

Web Crawler is a Python project designed to scrape all eSIM data from a specified website. This project utilizes the BeautifulSoup4 library for HTML parsing and data extraction.

## Description

The goal of this project is to perform web crawling on a specified website and gather all available eSIM-related information. The collected data can then be stored in a format suitable for further processing.

## Installation

To install and run this project, you only need Python and the BeautifulSoup4 library. Follow these steps to get started:

1. Clone this repository:
    ```bash
    git clone https://github.com/Ninoambaraa/crawler-engine.git
    cd web-crawler
    ```

2. Install the dependencies:
    ```bash
    pip install beautifulsoup4
    ```

## Usage

To run the web crawler, simply execute the provided Python script. For example:
    ```bash
    python main.py
    ```

Make sure to replace `main.py` with the actual name of your script file.

## Dependencies

- Python
- BeautifulSoup4

## License

This project does not have a specific license.

## Contact

For further questions or information, please reach out as needed.

```
{
    "fragments": {
        "div.widget_shopping_cart_content": "<div class=\"widget_shopping_cart_content\">\n\n\t<p class=\"woocommerce-mini-cart__empty-message\">No products in the cart.<\/p>\n\n\n<\/div>",
        ".contador-carrito": "<span class=\"contador-carrito\">0<\/span>",
        ".contador-productos-carrito": 0,
        ".shopping-cart__products": "<div class=\"shopping-cart__products\"><div class=\"shopping-cart_loading hidden\"><img src=\"https:\/\/esim.holafly.com\/wp-content\/themes\/Holafly_v2-child\/recursos\/img\/cargando.gif\" loading=\"lazy\" decoding=\"async\"><\/div><\/div>",
        ".shopping-cart__total-cart": "<span class=\"shopping-cart__total-cart\" data-total=\"0\"><span class=\"woocommerce-Price-amount amount\"><bdi><span class=\"woocommerce-Price-currencySymbol\">$<\/span>0.00<\/bdi><\/span><\/span>",
        "shopify_cart": [
            "holafly-esim.myshopify.com",
            "9d74f543f9580e56b3468b3289971c41",
            []
        ]
    },
    "cart_hash": ""
}
```
