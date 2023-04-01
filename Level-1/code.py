'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def verifyorderquantities(amount: float, quantity: int):
    max_amount = 100000
    max_quantity = 100
    if (amount < -max_amount) or amount > max_amount or quantity < 0 or quantity > max_quantity:
        return False
    return True

def validorder(order: Order):
    net = 0
    
    for item in order.items:
        if verifyorderquantities(item.amount, item.quantity):
            if item.type == 'payment':
                net += item.amount
            elif item.type == 'product':
                net -= item.amount * item.quantity
            else:
                return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)

