#include QMK_KEYBOARD_H

// Bouton = DRAG_SCROLL en toggle (clic pour basculer scroll).
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT( DRAG_SCROLL )
};

// En plus : si le NumLock (piloté par une touche du clavier) est allume,
// la boule fait defiler. task_user s'execute AVANT le drag scroll du bouton,
// donc les deux ne se cumulent pas.
report_mouse_t pointing_device_task_user(report_mouse_t mouse_report) {
    if (host_keyboard_led_state().num_lock) {
        static float acc_h = 0, acc_v = 0;
        acc_h += (float)mouse_report.x / 64.0f;
        acc_v += (float)mouse_report.y / 64.0f;
        int8_t h = (int8_t)acc_h;
        int8_t v = (int8_t)acc_v;
        acc_h -= h;
        acc_v -= v;
        mouse_report.h = h;
        mouse_report.v = v;
        mouse_report.x = 0;
        mouse_report.y = 0;
    }
    return mouse_report;
}
