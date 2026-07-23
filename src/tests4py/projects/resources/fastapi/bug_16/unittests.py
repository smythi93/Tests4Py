import unittest
from enum import Enum
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(role, use_config):

        class RoleEnum(Enum):
            admin = 'admin'
            normal = 'normal'
            guest = 'guest'
            root = 'root'
            user = 'user'
            viewer = 'viewer'
            editor = 'editor'
            owner = 'owner'
            member = 'member'
            banned = 'banned'
        if use_config:

            class M(BaseModel):
                role: RoleEnum = None

                class Config:
                    use_enum_values = True
        else:

            class M(BaseModel):
                role: RoleEnum = None
        try:
            return jsonable_encoder(M(role=RoleEnum[role]))
        except Exception as e:
            return {'error': type(e).__name__}

    def test_diversity_1(self):
        result = self.run_test('admin', True)
        self.assertEqual({'role': 'admin'}, result)

    def test_diversity_2(self):
        result = self.run_test('user', True)
        self.assertEqual({'role': 'user'}, result)

    def test_diversity_3(self):
        result = self.run_test('banned', True)
        self.assertEqual({'role': 'banned'}, result)

    def test_diversity_4(self):
        result = self.run_test('normal', True)
        self.assertEqual({'role': 'normal'}, result)

    def test_diversity_5(self):
        result = self.run_test('root', True)
        self.assertEqual({'role': 'root'}, result)

    def test_diversity_6(self):
        result = self.run_test('member', True)
        self.assertEqual({'role': 'member'}, result)

    def test_diversity_7(self):
        result = self.run_test('editor', True)
        self.assertEqual({'role': 'editor'}, result)

    def test_diversity_8(self):
        result = self.run_test('viewer', True)
        self.assertEqual({'role': 'viewer'}, result)

    def test_diversity_9(self):
        result = self.run_test('owner', True)
        self.assertEqual({'role': 'owner'}, result)

    def test_diversity_10(self):
        result = self.run_test('guest', True)
        self.assertEqual({'role': 'guest'}, result)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(role, use_config):

        class RoleEnum(Enum):
            admin = 'admin'
            normal = 'normal'
            guest = 'guest'
            root = 'root'
            user = 'user'
            viewer = 'viewer'
            editor = 'editor'
            owner = 'owner'
            member = 'member'
            banned = 'banned'
        if use_config:

            class M(BaseModel):
                role: RoleEnum = None

                class Config:
                    use_enum_values = True
        else:

            class M(BaseModel):
                role: RoleEnum = None
        try:
            return jsonable_encoder(M(role=RoleEnum[role]))
        except Exception as e:
            return {'error': type(e).__name__}

    def test_diversity_1(self):
        result = self.run_test('user', False)
        self.assertEqual({'role': 'user'}, result)

    def test_diversity_2(self):
        result = self.run_test('guest', False)
        self.assertEqual({'role': 'guest'}, result)

    def test_diversity_3(self):
        result = self.run_test('viewer', False)
        self.assertEqual({'role': 'viewer'}, result)

    def test_diversity_4(self):
        result = self.run_test('owner', False)
        self.assertEqual({'role': 'owner'}, result)

    def test_diversity_5(self):
        result = self.run_test('member', False)
        self.assertEqual({'role': 'member'}, result)

    def test_diversity_6(self):
        result = self.run_test('banned', False)
        self.assertEqual({'role': 'banned'}, result)

    def test_diversity_7(self):
        result = self.run_test('editor', False)
        self.assertEqual({'role': 'editor'}, result)

    def test_diversity_8(self):
        result = self.run_test('root', False)
        self.assertEqual({'role': 'root'}, result)

    def test_diversity_9(self):
        result = self.run_test('admin', False)
        self.assertEqual({'role': 'admin'}, result)

    def test_diversity_10(self):
        result = self.run_test('normal', False)
        self.assertEqual({'role': 'normal'}, result)
