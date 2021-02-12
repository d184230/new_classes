class UserError(BaseException):
    """ Ошибки в классе пользователя """

    def __init__(self, text):
        self.txt = text


class UserErrorInit(UserError):
    pass


class UserClass:
    """Пользователь и все данные по нему
    Атрибуты:
        • platform - платформа пользователя (vk, vb, tg, wh)
        • user_id - id пользователя внутри платформы
        • social_id - {platform}_{user_id}
        • project_hash - хеш проекта пользователя
        • user_marker - {project_hash}::{platform}_{user_id}
        • uuid - bots__{project_hash}__{platform}__{user_id}
    """

    def __init__(self, platform, user_id, project_hash):
        """ Инициализация по  platform, user_id, project_hash"""
        if not (platform and user_id and project_hash):
            raise UserErrorInit(
                'Недостаточно данных для инициализации пользователя: platform = {}, user_id = {}, project_hash = {}'.format(platform,
                                                                                                                            user_id,
                                                                                                                            project_hash))
        self.platform = platform
        self.user_id = user_id
        self.social_id = '{}_{}'.format(platform, user_id)
        self.project_hash = project_hash
        self.user_marker = '{}::{}'.format(project_hash, self.social_id)
        self.uuid = 'bots__{}__{}__{}'.format(project_hash, platform, user_id)

    @classmethod
    def from_user_marker(cls, user_marker):
        """ Инициализация по user_marker """
        if len(user_marker.split("::")) != 2:
            raise UserErrorInit('user_marker имеет неверный формат, ошибка в разделителе "::": {}'.format(user_marker))
        project_hash, social_id = user_marker.split("::")
        if len(social_id.split('_')) != 2:
            raise UserErrorInit('user_marker имеет неверный формат, ошибка в разделителе "_": {}'.format(user_marker))
        platform, user_id = social_id.split('_')
        return cls(platform, user_id, project_hash)
