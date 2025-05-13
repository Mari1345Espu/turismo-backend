Feature: Crear lugares turísticos
  Solo expertos o administradores pueden crear lugares

  Scenario: Usuario normal no puede crear lugar
    Given un usuario con rol "normal" y clave "test1234"
    And estoy autenticado como "normal@example.com"
    When intento crear un lugar con nombre "Mirador del Sol"
    Then la respuesta debe ser 403

  Scenario: Usuario experto puede crear lugar
    Given un usuario con rol "experto" y clave "test1234"
    And estoy autenticado como "experto@example.com"
    When intento crear un lugar con nombre "Mirador del Sol"
    Then la respuesta debe ser 201
