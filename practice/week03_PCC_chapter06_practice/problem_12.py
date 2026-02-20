# You're reviewing which settings are configured in a system.
#
# You have a settings dictionary:
# - auto_save: True
# - theme: 'light'
# - font_size: 14
# - spell_check: False
#
# Print just the names of all the settings (the keys), one per line.
# Don't print the values.

settings = {
    'auto_save':True,
    'theme':'light',
    'font_size':14,
    'spell_check':False
}

for key in settings.keys():
    print(f'{key}')