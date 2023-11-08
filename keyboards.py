import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

main = VkKeyboard(one_time=True)
main.add_button('Создать жалобу на бандита/лидера☢', color=VkKeyboardColor.PRIMARY)
main.add_button('Создать жалобу на лидера☣', color=VkKeyboardColor.POSITIVE)
main.add_line()  # создание новой строки
main.add_button('Кнопка 3', color=VkKeyboardColor.NEGATIVE)
main.add_button('Кнопка 4', color=VkKeyboardColor.SECONDARY)

nick = VkKeyboard(one_time=True)
nick.add_button('Да✅', color=VkKeyboardColor.POSITIVE)
nick.add_button('Нет⛔', color=VkKeyboardColor.NEGATIVE)

success = VkKeyboard(one_time=True)
success.add_button('Готово✅', color=VkKeyboardColor.POSITIVE)