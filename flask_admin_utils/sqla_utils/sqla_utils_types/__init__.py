from color_type import formatter as color_formatter
from password_type import formatter as password_formatter

from flask.ext.admin.model import typefmt

from sqlalchemy_utils import Password
BASE_FORMATTERS = typefmt.BASE_FORMATTERS.update({Password: password_formatter})

try:
    from colour import Color
    BASE_FORMATTERS = typefmt.BASE_FORMATTERS.update({Color: color_formatter})
except ImportError:
    pass
