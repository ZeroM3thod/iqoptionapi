from iqoptionapi.ws.chanels.base import Base
import iqoptionapi.global_value as global_value

class Blitz_open_option(Base):
    name = "sendMessage"

    def __call__(self, user_balance_id, active_id, option_type_id, direction, expired, price, value, profit_percent, expiration_size, request_id):
        data = {
            "name": "binary-options.open-option",
            "version": "2.0",
            "body": {
                "user_balance_id": int(user_balance_id),
                "active_id": int(active_id),
                "option_type_id": int(option_type_id),
                "direction": str(direction).lower(),
                "expired": int(expired),
                "refund_value": 0,
                "price": float(price),
                "value": int(value),
                "profit_percent": int(profit_percent),
                "expiration_size": int(expiration_size)
            }
        }
        self.send_websocket_request(self.name, data, str(request_id))
