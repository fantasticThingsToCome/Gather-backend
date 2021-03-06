from flask_restful import Resource, reqparse
from flask import request
import stripe

BLANK_ERROR = "'{}' cannot be blank."


class StripeCharge(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("amount", type=int, required=True, help=BLANK_ERROR)
    parser.add_argument("token", type=str, required=True, help=BLANK_ERROR)

    @classmethod
    def post(cls):
        data = StripeCharge.parser.parse_args()

        stripe.api_key = "sk_test_E8MBFdfr7DGN0cSwRtIMrSqr"

        charge = stripe.Charge.create(
            amount=data["amount"],
            currency="usd",
            source=data["token"],
            description="test charge",
        )
        return charge
