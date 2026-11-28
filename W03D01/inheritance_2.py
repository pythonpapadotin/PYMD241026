# # marketplaces : Amazon, Shopify, Flipkart, Ebay
#
# # DELL Manager You only want to see the Orders that are Delivery in Progress
# class Marketplace:
#     def get_orders(self):
#         raise NotImplementedError
#
#
# class Amazon(Marketplace):
#     def get_orders(self):
#         pass
#
#
# class Shopify(Marketplace):
#     def get_orders(self):
#         pass
#
#
# class Flipkart(Marketplace):
#     def get_orders(self):
#         pass
#
#
# class Ebay(Marketplace):
#     def get_orders(self):
#         pass
#
#
# def show_all_orders_with_status_filter(status):
#     list_of_marketplaces = [Amazon(), Shopify(), Flipkart(),
#                             Ebay()]
#     all_orders = []
#     for mp in list_of_marketplaces:
#         orders = mp.get_orders(status)
#         all_orders.append(orders)
#     return all_orders
