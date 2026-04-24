from compuestos.persona import persona

juan = persona("juan", "castellanos",15)
juan.mostrarpersona()

leidy = persona("leidy", "Alvarez", 18)
leidy.mostrarpersona()

leidy.apellido = "perez"
leidy.mostrarpersona()

juan = leidy 

juan.mostrarpersona()

