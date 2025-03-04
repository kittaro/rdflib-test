import rdflib

# Загружаем онтологию из файла
g = rdflib.Graph()
g.parse("gadgets.rdf", format="xml")

NS = rdflib.Namespace("http://www.example.org/gadgets#")

def recommend_manufacturers(gadget_type: str, price_segment: str):
    """
    Функция возвращает список производителей, которые имеют тип gadget_type
    и принадлежат к ценовому сегменту price_segment.
    """
    query = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX : <http://www.example.org/gadgets#>
    SELECT DISTINCT ?manufacturer WHERE {{
        ?manufacturer rdf:type :Manufacturer .
        ?manufacturer rdf:type :{gadget_type} .
        ?manufacturer rdf:type :{price_segment} .
    }}
    """
    results = g.query(query)
    return [str(row.manufacturer).split("#")[-1] for row in results]

if __name__ == "__main__":
    print("Программа рекомендации производителей гаджетов")
    gadget_type = input("Введите тип гаджета (Ноутбук, Смартфон, Планшет): ").strip()
    price_segment = input("Введите ценовой сегмент (Низкий, Средний, Высокий): ").strip()

    recommendations = recommend_manufacturers(gadget_type, price_segment)
    
    if recommendations:
        print(f"\nРекомендуемые бренды для {gadget_type} в ценовом сегменте {price_segment}:")
        for m in recommendations:
            print(f"- {m}")
    else:
        print("\nНет рекомендаций по заданным критериям.")
