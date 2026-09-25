# 	<Имя основного файла>/core_module // ☭
# MichiTheCat-RedStar (c) 2026


# Импорт модулей
from importlib import import_module


# Основной код
def ImportModule(module:str, function:str, namespace:dict=None, helps:str=None):
	'Импорт модуля; на месте namespace обычно globals()'
	
	print(f'Попытка импорта {module}.{function}...', end='', flush=True)
	try:
		mod = import_module(module)
		func = getattr(mod, function)
	except (ModuleNotFoundError, ImportError, AttributeError):
		print('\b'*3, '[Неудачно!]\n')
		if helps:
			raise ImportError(f'Попробуйте: {helps}\n') from None
		else:
			raise
	except Exception as e:
		print('\b'*3, '[Неудачно!]\nОшибка:', e, '\n')
		raise
	else:
		print('\b'*3, '[Успешно.]')
		if namespace is not None:
			namespace[function] = func
		return func


# TEST
if __name__ == '__main__':
	ImportModule('pprint', 'pprint', globals(), 'пересобрать python')
	pprint({'test': 1})
	
	sqrt = ImportModule('math', 'sqrt', helps='проверить math')
	print('sqrt(16) =', sqrt(16))
	
	ImportModule('module_not_exist', 'function', globals(), 'ничего. Серьёзно. Типа, всё работает, если вы видите это.')
