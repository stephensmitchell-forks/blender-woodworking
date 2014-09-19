# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENSE BLOCK *****


# ##### BEGIN AUTOGENERATED I18N SECTION #####
# NOTE: You can safely move around this auto-generated block (with the begin/end markers!),
#       and edit the translations by hand.
#       Just carefully respect the format of the tuple!

# Tuple of tuples ((msgctxt, msgid), (sources, gen_comments), (lang, translation, (is_fuzzy, comments)), ...)
translations_tuple = (
    (("*", ""),
     ((), ()),
     ("fr_FR", "Project-Id-Version: wood work 1.0 (0)\n",
               (False,
                ("Blender's translation file (po format).",
                 "Copyright (C) 2014 The Blender Foundation.",
                 "This file is distributed under the same license as the Blender package.",
                 "FIRST AUTHOR <EMAIL@ADDRESS>, YEAR."))),
    ),
    (("Operator", "Tenon"),
     (("bpy.types.MESH_OT_tenon",),
      ()),
     ("fr_FR", "Tenon",
               (False, ())),
    ),
    (("*", "Creates a tenon given a face"),
     (("bpy.types.MESH_OT_tenon",),
      ()),
     ("fr_FR", "Créer un tenon à partir d'une face",
               (False, ())),
    ),
    (("*", "Woodworking"),
     (("bpy.types.woodworking_main_panel",),
      ()),
     ("fr_FR", "Travail du bois",
               (False, ())),
    ),
    (("*", "Haunch value type"),
     (("bpy.types.TenonHeightPropertyGroup.haunch_type",),
      ()),
     ("fr_FR", "Type de valeur pour le renfort",
               (False, ())),
    ),
    (("*", "Give value to haunch depth"),
     (("bpy.types.TenonHeightPropertyGroup.haunch_type:'value'",),
      ()),
     ("fr_FR", "Renseigner la valeur pour le renfort d'épaulement",
               (False, ())),
    ),
    (("*", "Set haunch depth by percentage"),
     (("bpy.types.TenonHeightPropertyGroup.haunch_type:'percentage'",),
      ()),
     ("fr_FR", "Définir la hauteur du renfort en pourcentage",
               (True, ())),
    ),
    (("*", "Tenon height relative to length side"),
     (("bpy.types.TenonHeightPropertyGroup.value",
       "bpy.types.TenonHeightPropertyGroup.percentage"),
      ()),
     ("fr_FR", "Hauteur du tenon relative à la longueur de la face",
               (False, ())),
    ),
    (("*", "Shoulder"),
     (("bpy.types.TenonHeightPropertyGroup.shoulder_percentage",
       "bpy.types.TenonHeightPropertyGroup.shoulder_value",
       "bpy.types.TenonThicknessPropertyGroup.shoulder_percentage",
       "bpy.types.TenonThicknessPropertyGroup.shoulder_value"),
      ()),
     ("fr_FR", "Epaulement",
               (False, ())),
    ),
    (("*", "Tenon shoulder (relative to length side)"),
     (("bpy.types.TenonHeightPropertyGroup.shoulder_percentage",),
      ()),
     ("fr_FR", "Epaulement du tenon (valeur relative à la longueur)",
               (False, ())),
    ),
    (("*", "Height shoulder type"),
     (("bpy.types.TenonHeightPropertyGroup.shoulder_type",
       "scripts/addons/woodwork/tenon.py:270"),
      ()),
     ("fr_FR", "Type d'épaulement pour la hauteur",
               (False, ())),
    ),
    (("*", "Give value to shoulder height"),
     (("bpy.types.TenonHeightPropertyGroup.shoulder_type:'value'",),
      ()),
     ("fr_FR", "Renseigner la valeur de l'épaulement pour la hauteur",
               (False, ())),
    ),
    (("*", "Set shoulder height by percentage"),
     (("bpy.types.TenonHeightPropertyGroup.shoulder_type:'percentage'",),
      ()),
     ("fr_FR", "Donner la valeur de l'épaulement pour la hauteur en pourcentage",
               (False, ())),
    ),
    (("*", "Height type"),
     (("bpy.types.TenonHeightPropertyGroup.type",
       "scripts/addons/woodwork/tenon.py:261"),
      ()),
     ("fr_FR", "Type de valeur pour la hauteur",
               (False, ())),
    ),
    (("*", "Max. height"),
     (("bpy.types.TenonHeightPropertyGroup.type:'max'",),
      ()),
     ("fr_FR", "Hauteur maximale",
               (False, ())),
    ),
    (("*", "Set height to the maximum length"),
     (("bpy.types.TenonHeightPropertyGroup.type:'max'",),
      ()),
     ("fr_FR", "Définir la hauteur du tenon comme étant celle de la longueur de la face",
               (False, ())),
    ),
    (("*", "Give value to height"),
     (("bpy.types.TenonHeightPropertyGroup.type:'value'",),
      ()),
     ("fr_FR", "Renseigner la valeur de la hauteur du tenon",
               (False, ())),
    ),
    (("*", "Set height by percentage"),
     (("bpy.types.TenonHeightPropertyGroup.type:'percentage'",),
      ()),
     ("fr_FR", "Définir la hauteur du tenon en pourcentage",
               (False, ())),
    ),
    (("*", "Haunch depth"),
     (("bpy.types.TenonHeightPropertyGroup.haunch_depth_percentage",
       "bpy.types.TenonHeightPropertyGroup.haunch_depth_value",
       "bpy.types.TenonHeightPropertyGroup.haunch_depth_value"),
      ()),
     ("fr_FR", "Profondeur du renfort d'épaulement",
               (False, ())),
    ),
    (("*", "Haunch depth (relative to tenon depth)"),
     (("bpy.types.TenonHeightPropertyGroup.haunch_depth_percentage",),
      ()),
     ("fr_FR", "Profondeur du renfort d'épaulement (relative à la profondeur du tenon)",
               (False, ())),
    ),
    (("*", "Haunched"),
     (("bpy.types.TenonHeightPropertyGroup.haunched",),
      ()),
     ("fr_FR", "Renfort d'épaulement",
               (False, ())),
    ),
    (("*", "Add a little stub tenon at the top of the joint"),
     (("bpy.types.TenonHeightPropertyGroup.haunched",),
      ()),
     ("fr_FR", "Ajoute un renfort au tenon",
               (False, ())),
    ),
    (("*", "Tenon shoulder on length side"),
     (("bpy.types.TenonHeightPropertyGroup.shoulder_value",),
      ()),
     ("fr_FR", "Epaulement du tenon sur la longueur",
               (False, ())),
    ),
    (("*", "Centered"),
     (("bpy.types.TenonHeightPropertyGroup.centered",
       "bpy.types.TenonThicknessPropertyGroup.centered"),
      ()),
     ("fr_FR", "Centré",
               (False, ())),
    ),
    (("*", "Specify if tenon is centered on length side"),
     (("bpy.types.TenonHeightPropertyGroup.centered",),
      ()),
     ("fr_FR", "Indique si le tenon est centré en longueur",
               (False, ())),
    ),
    (("*", "Reverse shoulder"),
     (("bpy.types.TenonHeightPropertyGroup.reverse_shoulder",
       "bpy.types.TenonThicknessPropertyGroup.reverse_shoulder"),
      ()),
     ("fr_FR", "Renverser l'épaulement",
               (False, ())),
    ),
    (("*", "Specify shoulder for the other side"),
     (("bpy.types.TenonHeightPropertyGroup.reverse_shoulder",
       "bpy.types.TenonThicknessPropertyGroup.reverse_shoulder"),
      ()),
     ("fr_FR", "Indique que l'épaulement se situe de l'autre côté",
               (False, ())),
    ),
    (("*", "Tenon depth"),
     (("bpy.types.TenonPropertyGroup.depth_value",),
      ()),
     ("fr_FR", "Profondeur du tenon",
               (False, ())),
    ),
    (("*", "Tenon thickness (relative to width side)"),
     (("bpy.types.TenonThicknessPropertyGroup.value",
       "bpy.types.TenonThicknessPropertyGroup.percentage"),
      ()),
     ("fr_FR", "Epaisseur du tenon relative à la largeur de la face",
               (False, ())),
    ),
    (("*", "Tenon shoulder (relative to width side)"),
     (("bpy.types.TenonThicknessPropertyGroup.shoulder_percentage",),
      ()),
     ("fr_FR", "Epaulement du tenon relatif à la largeur de la face",
               (False, ())),
    ),
    (("*", "Thickness shoulder type"),
     (("bpy.types.TenonThicknessPropertyGroup.shoulder_type",
       "scripts/addons/woodwork/tenon.py:245"),
      ()),
     ("fr_FR", "Type de valeur pour l'épaisseur de l'épaulement",
               (False, ())),
    ),
    (("*", "Give value to shoulder thickness"),
     (("bpy.types.TenonThicknessPropertyGroup.shoulder_type:'value'",),
      ()),
     ("fr_FR", "Renseigner la valeur de l'épaulement pour l'épaisseur",
               (False, ())),
    ),
    (("*", "Set thickness shoulder by percentage"),
     (("bpy.types.TenonThicknessPropertyGroup.shoulder_type:'percentage'",),
      ()),
     ("fr_FR", "Définir l'épaulement pour l'épaisseur en pourcentage",
               (False, ())),
    ),
    (("*", "Thickness type"),
     (("bpy.types.TenonThicknessPropertyGroup.type",
       "scripts/addons/woodwork/tenon.py:236"),
      ()),
     ("fr_FR", "Type de valeur pour l'épaisseur",
               (False, ())),
    ),
    (("*", "Max. thickness"),
     (("bpy.types.TenonThicknessPropertyGroup.type:'max'",),
      ()),
     ("fr_FR", "Epaisseur maximale",
               (False, ())),
    ),
    (("*", "Set thickness to the maximum width"),
     (("bpy.types.TenonThicknessPropertyGroup.type:'max'",),
      ()),
     ("fr_FR", "Définir l'épaisseur du tenon comme étant celle de la largeur de la face",
               (False, ())),
    ),
    (("*", "Give value to thickness"),
     (("bpy.types.TenonThicknessPropertyGroup.type:'value'",),
      ()),
     ("fr_FR", "Renseigner la valeur de l'épaisseur",
               (False, ())),
    ),
    (("*", "Set thickness by percentage"),
     (("bpy.types.TenonThicknessPropertyGroup.type:'percentage'",),
      ()),
     ("fr_FR", "Définir l'épaisseur en pourcentage",
               (False, ())),
    ),
    (("*", "Specify if tenon is centered on width side"),
     (("bpy.types.TenonThicknessPropertyGroup.centered",),
      ()),
     ("fr_FR", "Indique que le tenon est centré sur la largeur de la face",
               (False, ())),
    ),
    (("*", "Tenon shoulder on width side"),
     (("bpy.types.TenonThicknessPropertyGroup.shoulder_value",),
      ()),
     ("fr_FR", "Valeur de l'épaulement sur le côté de la largeur",
               (False, ())),
    ),
    (("*", "Joints"),
     (("scripts/addons/woodwork/main_panel.py:15",),
      ()),
     ("fr_FR", "Assemblages",
               (False, ())),
    ),
    (("*", "Depth"),
     (("scripts/addons/woodwork/tenon.py:286",),
      ()),
     ("fr_FR", "Profondeur",
               (False, ())),
    ),
    (("*", "You must select a face for the tenon."),
     (("scripts/addons/woodwork/tenon.py:199",),
      ()),
     ("fr_FR", "Vous devez sélectionner une face pour créer le tenon.",
               (False, ())),
    ),
    (("*", "Selected face is not quad."),
     (("scripts/addons/woodwork/tenon.py:205",),
      ()),
     ("fr_FR", "La face sélectionnée n'est pas un quadrangle.",
               (False, ())),
    ),
    (("*", "Selected face is not planar."),
     (("scripts/addons/woodwork/tenon.py:211",),
      ()),
     ("fr_FR", "La face sélectionnée doit est plane.",
               (False, ())),
    ),
    (("*", "Selected face is not rectangular."),
     (("scripts/addons/woodwork/tenon.py:216",),
      ()),
     ("fr_FR", "La face sélectionnée doit être rectangulaire.",
               (False, ())),
    ),
    (("*", "Width side"),
     (("scripts/addons/woodwork/tenon.py:231",
       "scripts/addons/woodwork/tenon.py:233"),
      ()),
     ("fr_FR", "Côté de la largeur",
               (False, ())),
    ),
    (("*", "Position"),
     (("scripts/addons/woodwork/tenon.py:242",
       "scripts/addons/woodwork/tenon.py:267"),
      ()),
     ("fr_FR", "Position",
               (False, ())),
    ),
    (("*", "Length side"),
     (("scripts/addons/woodwork/tenon.py:256",
       "scripts/addons/woodwork/tenon.py:258"),
      ()),
     ("fr_FR", "Côté de la longueur",
               (False, ())),
    ),
    (("*", "Size of length size shoulder and tenon height are too long."),
     (("scripts/addons/woodwork/tenon.py:413",),
      ()),
     ("fr_FR", "La dimension de l'épaulement côté longueur et la hauteur du tenon sont trop longs.",
               (False, ())),
    ),
    (("*", "Size of width size shoulder and tenon thickness are too long."),
     (("scripts/addons/woodwork/tenon.py:419",),
      ()),
     ("fr_FR", "La dimension de d'épaulement côté largeur et l'épaisseur du tenon sont trop longs.",
               (False, ())),
    ),
    (("*", "Haunch depth type"),
     (("scripts/addons/woodwork/tenon.py:279",),
      ()),
     ("fr_FR", "Type de valeur pour le renfort",
               (False, ())),
    ),
)

translations_dict = {}
for msg in translations_tuple:
    key = msg[0]
    for lang, trans, (is_fuzzy, comments) in msg[2:]:
        if trans and not is_fuzzy:
            translations_dict.setdefault(lang, {})[key] = trans

# ##### END AUTOGENERATED I18N SECTION #####

import bpy

def register(module_name):
    bpy.app.translations.register(module_name, translations_dict)

def unregister(module_name):
    bpy.app.translations.unregister(module_name)
