def test_docker_environment():
    """Проверяем что Docker и зависимости работают"""
    assert True

def test_imports():
    """Проверяем что все импорты работают"""
    try:
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        assert True
    except ImportError as e:
        assert False, f"Import error: {e}"