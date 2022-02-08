{
    'name': "Sale Order Force ",  #tên module
    'summary': """Sale Order Force Code """, #Mô tả ngắn gọn
    'description': """Sale order code """,#Mô tả
    'author': "Vu", #Tác giả
    'website': "https://www.facebook.com/vutran1305",
    'category': 'Uncategorized', #Loại modult
    'version': '0.1', #Phiên bản
    'depends': [
        'base','product','sale','contacts'
    ], #dependcy của module  sẽ phụ thuộc vào những app / module khác nào , khi để product thì khi cài module này  thì sẽ cài product
    'data': [
        'security/ir.model.access.csv',
            'security/security.xml',
            'views/customer_view.xml',
            'views/sale_order_inherit.xml',
            'wizard/sale_code_update.xml',
            'views/show_discount_code_on_my_cart.xml'
             ], #Chứa
                # các view , file xml
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}