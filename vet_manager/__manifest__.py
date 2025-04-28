{  # pylint: disable=C8101,C8103
    "name": "Gerenciador de Clínica Veterinária",
    "description": "Adapta o Odoo para gerir uma clínica veterinária",
    "category": 'Services', 
    "version": "17.0.1.0.1",
    "author": "aquiles",
    "depends": ["base", "web"],
    "data": ["views/animal.xml"],  
    "installable": True,  
    "auto_install": False,
    "application": True
}
