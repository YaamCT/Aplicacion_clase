import streamlit as st
st.title(":cow: Tipos de alimentación :carrot:")
st.sidebar.write("La alimentación es un proceso en el cual los seres vivos consumen diferentes tipos de alimentos para obtener de estos los nutrientes necesarios para sobrevivir y realizar todas las actividades necesarias del día a día.")
st.sidebar.image("https://www.gob.mx/cms/uploads/article/main_image/43779/Alimentaci_n-Alimentos-Dieta.jpg" ,width=300)
with st.sidebar:
        st.write("Integrantes:")
        sr.write("Julieta Yamileth Cruz Trillo 179473")
        st.write("Desiree Valenzuela González 330004")
        st.write("Universidad Autónoma de Chihuahua")
        st.write("Facultad de ciencias Químicas")
        st.write("Curso de programación")
        st.write("Docente: José Manuel Nápoles Duarte")
        

col1,col2,col3 = st.columns( [5,5,5] )
if col1.button("Omnívora"):
  col1.image("http://2.bp.blogspot.com/-JZPx97Aq3PU/VE0zdgiTXMI/AAAAAAAAFR4/-MfJGeMyprc/s1600/Nutricion-Dietas-Piramide-alimenticion-saludable-SENC.jpg",width=280)

if col2.button("Vegetarina"):
  col2.image("https://unionvegetariana.org/wp-content/uploads/2018/06/Piram_vegetariana.jpg",width=280)

if col3.button("Vegana"):
  col3.image("https://mundovegano.org/wp-content/uploads/2017/11/piramide-vegana.jpg",width=280)


st.write("De acuerdo a tu IMC podrás conocer qué tipos de alimentos son los que debes consumir mayormente para mantener una dieta saludable. :fork_and_knife:")
st.write("¡Calcula tu IMC para conocerlos!")

estatura=st.number_input("Escribe tu estatura en metros",1.0)
st.write(estatura)
masa=st.number_input("Escribe tu masa en kg",20)
#st.write(masa)

imc = masa/estatura**2
st.header(imc)

if imc<18.5:
  st.header("Peso por debajo del normal :worried:")
  st.write("Tendrás que comer con más frecuencia (5-6 veces al día), aumentar tu ingesta de proteínas de calidad; carnes magras y blancas, consumir alimentos ricos en nutrientes cómo panes, pastas y cereales integrales, licuados hechos de leche y fruta fresca, grasas saludables cómo aceite de oliva extra virgen, aguacate y semillas.")

if imc>18.5 and imc <24.9:
  st.header("Peso normal :grinning:")
  st.write("Tu dieta incluye mayormente alimentos con proteínas como carnes magras, huevos, pollo, mariscos. También es rica en frutas, verduras, legumbres (frijoles y guisantes). Contiene poca cantidad de grasas saturadas, grasas trans, colesterol, sal y azúcares agregados. Continua así :+1:.")

if imc>25 and imc<29.9:
  st.header("Sobrepeso :sweat_smile:")
  st.write("Tu dieta deberá consistir de abundantes frutas y verduras (al menos 5 porciones al día),  leche y yogures desnatados, carnes magras y blancas cocidas al vapor o a la plancha, evitar alimentos ricos en grasa saturada como los embutidos, en su lugar, consumir grasas vegetales como aceite de oliva extra virgen, aguacate y frutos secos,  beber al menos 2 litros de agua al día y restringir los alimentos con alta concentración de azúcares: jugos, refrescos, bebidas energéticas y cereales de caja.")

if imc>30 and imc<34.9:
  st.header("Obesidad grado I :neutral_face:")
  st.write("Deberás incluir en tu dieta abundantes frutas y verduras crudas o cocidas (al menos 5 unidades al día), cereales integrales, carnes y pescados magros cocinados al horno o al vapor, disminuir el consumo de sal y alcohol y  beber al menos 2 litros de agua diariamente.")

if imc>35 and imc<39.9:
  st.header("Obesidad grado II :anguished:")
  st.write("Deberás consumir mínimo 2 porciones de fruta diariamente, incluir en todas tus comidas abundante verdura, cocinar al vapor carnes magras bajas en grasas como pollo y pescado, beber al menos 2 litros de agua diariamente y evitar el consumo de alimentos refinados y ultraprocesados.")

if imc>40:
  st.header("Obesidad grado III :cold_sweat:")
  st.write("Tu dieta deberá incluir abundantes frutas y verduras (al menos 5 unidades al día), consumir diariamente 2 litros de agua, lácteos descremados, carnes magras y blancas cocidas al vapor o al horno, grasas vegetales tales como aguacate y semillas.")


if col1.button("¿En qué consiste una dieta omnívora?"):
  col1.write("Es el tipo de alimentación que más personas en el mundo practican y se caracteriza por la universalidad, permitiendo al individuo el consumo de todo tipo de productos tanto de origen animal como vegetal. Al no tener restricción alguna, puede llegar a ser causante de un desequilibrio alimentario, llevando a consumir de forma excesiva grasas saturadas, azúcares, sodio y carbohidratos; desencadenando en enfermedades cardiovasculares y problemas de obesidad.")

if col2.button("¿En qué consiste una dieta vegetariana?"):
  col2.write("En este régimen alimentario se eliminan de la dieta los productos cárnicos; sin embargo, permite algunos alimentos de origen animal, según el tipo de vegetarianismo que se practique. Por ejemplo: el ovovegetarianismo (permite el consumo de huevos), el lactovegetarianismo (permite la ingesta de lácteos) y el ovolactovegetarianismo (permite consumir huevos y lácteos). Los principales alimentos caracteristicos de esta dieta son: verduras, frutas, granos integrales, legumbres semillas y nueces.")

if col3.button("¿En qué consiste una dieta vegana?"):
  col3.write("En esta dieta se pretende la erradicación del sufrimiento y la explotación animal. Consiste en la supresión del consumo de alimentos y productos de origen animal, sus derivados y los que hayan sido probados en ellos. Existen empresas hoy en día, que proporcionan al vegano una amplia gama de productos elaborados a partir de ingredientes naturales y las cuales, pueden satisfacer sus necesidades sin renunciar a prácticamente ninguna delicia culinaria. Esta dieta básicamente consiste de cereales, frutas, hortalizas,legumbres, frutos secos y semillas")
