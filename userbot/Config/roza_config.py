#    جميع الحقوق لمطوري سورس ديو حصريا لهم فقط
#    اذا تخمط الملف اذكر الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة حسن وجيري

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from sample_config import Config  # noqa
elif os.path.exists("config.py"):
    from config import Development as Config  # noqa
