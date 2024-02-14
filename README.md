# No-Bloom-Fortnite-Cheat
Fortnite cheat to remove bloom from guns

Decomplied from binary and uploaded. (owner was charging 20 USD for these detected cheats which will get caught by anticheat).

1. Event Handling Functions (get_selected_gun, get_selected_mode):

  * These functions are triggered when a user selects a gun or mode from the GUI comboboxes.
  * get_selected_gun updates the current selected gun based on the event triggered by the combobox selection.
  * get_selected_mode updates the current selected mode similarly.

2. Profile Retrieval and GUI Setup (retrieve_profile, recoil_tab_create):

  * retrieve_profile retrieves profiles from the system, allowing users to select from existing profiles.
  * recoil_tab_create sets up the GUI components for the recoil tab, including labels, checkboxes, comboboxes, and buttons. It also binds event handlers to the comboboxes for gun and mode selection.

3. Attribute Handling and Profile Saving (check_recoil_var, check_random_var, profile_save):

  * These functions handle attributes related to recoil, randomization, and profile saving.
  * check_recoil_var and check_random_var update boolean variables based on checkbox states.
  * profile_save saves the current profile's attributes, including gun values and keybinds.

4. Key Press and Toggle Handling (check_toggle_pressed, check_mode_changes, check_key):
  * check_toggle_pressed monitors a specific key press (Numpad 0) to toggle the recoil checkbox in the GUI.
  * check_mode_changes checks for key presses (PAGE UP/DOWN) to change modes and updates the GUI accordingly.
  * check_key checks for a key press (INSERT) to toggle the visibility of the GUI.

5. Recoil Simulation (recoil_movement):
  * This function simulates recoil movements based on user-defined configurations.
  * It runs in a separate thread to continuously monitor key presses and toggle states.
  * Recoil movements are simulated by sending mouse events with specific values based on configured parameters such as fire rate, activation type, and randomization.
  * The function interacts with the GUI to update recoil status and current gun/mode being used.
