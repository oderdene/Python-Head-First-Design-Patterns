import functools
import time


# 1-Р ДАВХАРГА: Тохиргоог хүлээж авах (Factory)
def retry(times=3, delay=1):
    """
    Энэ хэсэг нь decorator-ийг өөрийг нь бүтээж буцаана.
    Бидний оруулсан @retry(times=3) гэх утгууд энд орж ирнэ.
    """

    # 2-Р ДАВХАРГА: Decorator өөрөө
    def actual_decorator(func):
        """
        Энд чимэглэгдэх гэж буй функц (func) орж ирнэ.
        """

        @functools.wraps(func)  # Энэ нь функцийн нэр, docstring-ийг эвдэхгүй байлгана
        # 3-Р ДАВХАРГА: Wrapper (Логик ажиллах хэсэг)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    # Жинхэнэ функцийг ажиллуулж үзнэ
                    return func(*args, **kwargs)
                except Exception as e:
                    print(
                        f"⚠️ Алдаа: {e}. {delay} сек хүлээгээд дахин оролдоё... ({i+1}/{times})"
                    )
                    time.sleep(delay)

            print("❌ Бүх оролдлого бүтэлгүйтлээ.")
            raise Exception("Retry failed")

        return wrapper

    return actual_decorator


# --- АШИГЛАЛТ ---


# Бид decorator-тоо 'times' болон 'delay' гэсэн утгуудыг дамжуулж байна
@retry(times=3, delay=2)
def connect_to_database():
    print("🔌 Бааз руу холбогдох гэж байна...")
    # Туршилтын зорилгоор албаар алдаа гаргая
    raise ConnectionError("Холболт тасарлаа!")


# Кодоо ажиллуулъя
try:
    connect_to_database()
    # retry(connect_to_database())
except:
    pass
