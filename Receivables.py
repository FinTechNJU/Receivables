class Receivables:
    """定义应收账款类
    """
    def __init__(self,rid,date,qty,omiga_debtor,debtor,creditor):
        #对应是应收账款的序号，应还日期，金额，债务人的信息：[(还款金额,拖欠金额)..(,)]
        #债务人，债权人
        self.rid=rid
        self.date=date
        self.qty=qty
        #计算债务人的还款比率：omiga
        piad=sum=0
        for i in omiga_debtor:
            paid+=i[0]
            sum+=i[1]
        self.rate_debtor=paid/sum
        #债务人和债权人的信息
        self.debtor=debtor
        self.creditor=creditor


class RecPricing(Receivables):
    """对应收账款的定价，被定价之后的应收账款
    """
    def __init__(self,recourse,rate_return,):
        #是否具有追索权，收益率
        self.recourse=recourse
        #具有追索权定价会相对高一点
        self.rate_return=rate_return

    def __str__(self):
        return 

    def expect_payment(self):
        # 
        return 

    def 

    def price(self):
        if self.recourse:
            return 
        else :
            return



