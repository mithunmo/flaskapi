import os
import unittest
from app import create_app
from app.model import PhoneNumber
from app.model import Account
from app.model import db
from app.model import check_valid
from app.model import check_param, ParamInValidException, ParamMissingException
from mockredis import MockRedis
from flask_redis import FlaskRedis
import json
import base64
from werkzeug.datastructures import Headers

class TestCase(unittest.TestCase):
    def setUp(self):
        app = create_app("dss")
        redis_con = FlaskRedis.from_custom_provider(MockRedis)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test12.db'
        #app.config['REDIS_URL'] = ""
        app.config["TESTING"] = True
        self.app = app.test_client()

        with app.app_context():
            db.drop_all()
            db.create_all()

            accnt1 = Account("p@ssword","mithun",)
            db.session.add(accnt1)
            db.session.commit()

            phnum = PhoneNumber("9886297837",accnt1.id)
            db.session.add(phnum)
            db.session.commit()

            phnum1 = PhoneNumber("7022620605",accnt1.id)
            db.session.add(phnum1)
            db.session.commit()

    def tearDown(self):
        pass


    def test_params(self):
        testparam = {"to":"9886297837","from":"9886297837","text":"hello"}
        r = check_param(testparam)
        assert r == True

    def test_params_missing(self):
        testparam = {"from":"9886297837","text":"hello"}
        self.assertRaises(ParamMissingException, check_param, testparam)

    def test_params_invalid(self):
        testparam = {"to":"11","from":"9886297837","text":"hello"}
        self.assertRaises(ParamInValidException, check_valid, testparam)

    def test_outbound(self):
        h = Headers()
        h.add('Authorization', 'Basic ' + base64.b64encode('mithun:p@ssword'))
        payload = {"to":"9886297837","from":"9886297837","text":"hello"}
        r = self.app.post('/outbound/sms',data=json.dumps(payload),content_type='application/json',headers=h)
        r= json.loads(r.data)
        assert r["message"] == "outbound sms ok"

    def test_outbound_invalid(self):
        h = Headers()
        h.add('Authorization', 'Basic ' + base64.b64encode('mithun:p@ssword'))
        payload = {"to":"9886297837","text":"hello"}
        r = self.app.post('/outbound/sms',data=json.dumps(payload),content_type='application/json',headers=h)
        r= json.loads(r.data)
        assert r["error"] == "from is missing"


    def test_inbound(self):
        h = Headers()
        h.add('Authorization', 'Basic ' + base64.b64encode('mithun:p@ssword'))
        payload = {"to":"9886297837","from":"9886297837","text":"hello"}
        r = self.app.post('/inbound/sms',data=json.dumps(payload),content_type='application/json',headers=h)
        r= json.loads(r.data)
        assert r["message"] == "inbound sms ok"


if __name__ == '__main__':
    unittest.main()