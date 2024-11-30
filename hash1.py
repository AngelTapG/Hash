class InventarioTienda:
    def __init__(self):
        
        self.inventario = {}
    
    def agregar_producto(self, codigo, nombre, cantidad, precio):
        """
        Agrega un producto al inventario usando el código como clave hash
        """
        self.inventario[codigo] = {
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }
    
    def buscar_producto(self, codigo):
        """
        Búsqueda de producto por código usando hash (diccionario)
        Complejidad temporal: O(1)
        """
        return self.inventario.get(codigo, None)
    
    def actualizar_cantidad(self, codigo, nueva_cantidad):
        """
        Actualiza la cantidad de un producto específico
        """
        if codigo in self.inventario:
            self.inventario[codigo]['cantidad'] = nueva_cantidad
            return True
        return False
    
    def eliminar_producto(self, codigo):
        """
        Elimina un producto del inventario
        """
        if codigo in self.inventario:
            del self.inventario[codigo]
            return True
        return False
    
    def listar_productos(self):
        """
        Lista todos los productos del inventario
        """
        for codigo, detalles in self.inventario.items():
            print(f"Código: {codigo}")
            print(f"Nombre: {detalles['nombre']}")
            print(f"Cantidad: {detalles['cantidad']}")
            print(f"Precio: ${detalles['precio']}")
            print("---")


def main():
    
    tienda = InventarioTienda()
    
    
    tienda.agregar_producto('A001', 'Laptop', 10, 1200.50)
    tienda.agregar_producto('B002', 'Smartphone', 25, 850.75)
    tienda.agregar_producto('C003', 'Tablet', 15, 450.25)
    
    
    producto = tienda.buscar_producto('B002')
    if producto:
        print("Producto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Cantidad: {producto['cantidad']}")
    
    
    tienda.actualizar_cantidad('A001', 8)
    
    
    print("\nInventario actual:")
    tienda.listar_productos()

if __name__ == "__main__":
    main()