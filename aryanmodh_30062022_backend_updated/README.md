AutoMate Sale Order Line
------------------------------------


* Odoo practical exam module.


Installation:
------------

* To install this module, you need to :-

  * Download the module and add it to your Odoo addons folder. Afterwards, log on to
your Odoo server and go to Apps Menu. Trigger the debug mode and update the 
list by clicking on the "Update Apps list" link. Now install the module by
clicking on the installation button.


Tasks Covered:
-------------
1. Add Product M2o and Qty in sale.order. onchange of Product and Qty, Order line
should be generated (If we select the same Product twice, we just need to update its
ordered qty. There will be only one product line on Sales Line)


2. Add Length field in Product.


3. In Sale order Line make customisation as follows:
    
    a. Add length and Total length field.
    
    b. Length should be filled automatically from Product.

    c. Total Length = Length * Qty

    d. Sub Total = Length * Qty * Unit Price.


4. In Invoice Lines make customisation as follows:

    a. Add length and Total length field.

    b. Length and Total Length should be filled automatically from Sale Order Line.


5. Add Length and Total Length field in Sale Order report.


Contributors:
-------------

* Aryan Modh
