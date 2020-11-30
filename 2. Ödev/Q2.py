class WebPush:
    def __init__(self, platform, optIn, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optIn = bool(optIn)
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def sendPush(self):
        print("{} Push gönderildi !".format(self.push_type))


class TriggerPush(WebPush):
    def __init__(self, trigger_page, platform, optIn, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optIn, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, send_date, platform, optIn, global_frequency_capping, start_date, end_date, language, push_type):
        super().__init__(platform, optIn, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, segment_name, platform, optIn, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optIn, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, price_info, Discount_rate, platform, optIn, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optIn, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.Discount_rate = float(Discount_rate)

    def discountPrice(self):
        discountAmount = self.price_info - (self.price_info * self.Discount_rate / 100)
        return discountAmount


class InstockPush(WebPush):
    def __init__(self, stock_info, platform, optIn, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optIn, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = bool(stock_info)

    def stockUpdate(self):
        if self.stock_info:
            self.stock_info = False
        elif not self.stock_info:
            self.stock_info = True
        else:
            print("Something went wrong")


TriggerPushExample = TriggerPush("https://www.google.com/", "Web", True, 2, "15/05/2020", "17/05/2020", "Turkish",
                                 "Trigger")
TriggerPushExample.sendPush()
BulkPushExample = BulkPush(1605104481, "Web", True, 4, "16/04/2020", "16/05/2020", "All language", "Bulk")
BulkPushExample.sendPush()
SegmentPushExample = SegmentPush("Purchase History", "Mobil", True, 3, "18/03/2019", "18/03/2020", "English", "Segment")
SegmentPushExample.sendPush()
PriceAlertPushExample = PriceAlertPush(1000, 25, "web", False, 1, "22/07/2019", "23/08/2020", "Turkish", "Price Alert")
PriceAlertPushExample.sendPush()
discount = PriceAlertPushExample.discountPrice()
print(discount)
InstockPushExample = InstockPush(True, "web", True, 4, "15/05/2020", "16/05/2020", "Arabic", "InStock")
InstockPushExample.sendPush()
InstockPushExample.stockUpdate()
print(InstockPushExample.stock_info)
