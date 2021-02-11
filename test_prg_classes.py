import unittest

from prg_classes import UserClass, UserErrorInit


class TestUserClass(unittest.TestCase):
    """ Тестирование класса UserClass """

    def test_init(self):
        """ Тестирование инициализации """
        user = UserClass('vk', '123', 'project_hash')
        self.assertEqual(user.project_hash, 'project_hash')
        self.assertEqual(user.platform, 'vk')
        self.assertEqual(user.social_id, 'vk_123')
        self.assertEqual(user.user_id, '123')
        self.assertEqual(user.uuid, 'bots__project_hash__vk__123')
        with self.assertRaises(UserErrorInit):
            UserClass('vk', '123', '')
        with self.assertRaises(UserErrorInit):
            UserClass('vk', '', 'project_hash')
        with self.assertRaises(UserErrorInit):
            UserClass('', '123', 'project_hash')

        user = UserClass.from_user_marker('project_hash::vk_123')
        self.assertEqual(user.project_hash, 'project_hash')
        self.assertEqual(user.platform, 'vk')
        self.assertEqual(user.social_id, 'vk_123')
        self.assertEqual(user.user_id, '123')
        self.assertEqual(user.uuid, 'bots__project_hash__vk__123')
        with self.assertRaises(UserErrorInit):
            UserClass.from_user_marker('project_hash')
        with self.assertRaises(UserErrorInit):
            UserClass.from_user_marker('project_hash::123')
        with self.assertRaises(UserErrorInit):
            UserClass.from_user_marker('project_hash::vk_124::test')
        with self.assertRaises(UserErrorInit):
            UserClass.from_user_marker('project_hash::vk_124_12432')


if __name__ == '__main__':
    unittest.main()
