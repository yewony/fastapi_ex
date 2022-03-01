# 환경별 변수를 넣는 공간
# 운영서버 / 개발서버 / QA를 수행하는 스테이징 서버 / 로컬
# 각 환경 별로 설정파일이 다르므로 그런 것들을 정의해줌. environment.py 같은?

from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = "mysql+pymysql://root:admin1234@localhost:3306/test?charset=utf8mb4"


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))

print(asdict(LocalConfig()))