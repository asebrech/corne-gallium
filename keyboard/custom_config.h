// Copyright 2019 Manna Harbour
// https://github.com/manna-harbour/miryoku

// This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

#pragma once

// Ce fork ne connait pas l'alphabet Gallium -> on le definit (identique au Gallium
// officiel de miryoku_zmk) et on force la couche de base dessus.

#define MIRYOKU_ALTERNATIVES_BASE_GALLIUM \
KC_B,              KC_L,              KC_D,              KC_C,              KC_V,              KC_J,              KC_Y,              KC_O,              KC_U,              KC_QUOT,            \
LGUI_T(KC_N),      LALT_T(KC_R),      LCTL_T(KC_T),      LSFT_T(KC_S),      KC_G,              KC_P,              LSFT_T(KC_H),      LCTL_T(KC_A),      LALT_T(KC_E),      LGUI_T(KC_I),       \
LT(U_BUTTON,KC_X), ALGR_T(KC_Q),      KC_M,              KC_W,              KC_Z,              KC_K,              KC_F,              KC_COMM,           ALGR_T(KC_DOT),    LT(U_BUTTON,KC_SLSH),\
U_NP,              U_NP,              LT(U_MEDIA,KC_ESC),LT(U_NAV,KC_SPC),  LT(U_MOUSE,KC_TAB),LT(U_SYM,KC_ENT),  LT(U_NUM,KC_BSPC), LT(U_FUN,KC_DEL),  U_NP,              U_NP

#define MIRYOKU_LAYER_BASE MIRYOKU_ALTERNATIVES_BASE_GALLIUM

// Layer Button : NumLock sur la case libre a cote de Shift (inner gauche)
// -> bascule le mode scroll du Ploopy (pont NumLock).
#define MIRYOKU_LAYER_BUTTON \
U_UND,   U_CUT,   U_CPY,   U_PST,   U_RDO,     U_RDO,   U_PST,   U_CPY,   U_CUT,   U_UND,   \
KC_LGUI, KC_LALT, KC_LCTL, KC_LSFT, KC_NUM,    U_NU,    KC_LSFT, KC_LCTL, KC_LALT, KC_LGUI, \
U_UND,   U_CUT,   U_CPY,   U_PST,   U_RDO,     U_RDO,   U_PST,   U_CPY,   U_CUT,   U_UND,   \
U_NP,    U_NP,    KC_BTN3, KC_BTN1, KC_BTN2,   KC_BTN2, KC_BTN1, KC_BTN3, U_NP,    U_NP
