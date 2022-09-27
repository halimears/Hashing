"""
Hash fonksiyonları aldıkları girdinin boyutundan bağımsız olarak belirli uzunluğa sahip bir çıktı üretirler.
Üretilen çıktı verilen girdiye özeldir. Aynı girdi ile sürekli aynı çıktı oluşur
ve iki farklı girdinin çıktısı ile birbiriyle aynı olamaz.
Genellikle web uygulamalarında kullanıcı parolalarını tutmak yerine Hash’lerinin alınıp veri tabanında saklanır.
Kullanıcının siteye kaydı sırasında verdiği parolanın hashi alınır, kullanıcı adı ile birlikte veri tabanında saklanır.

- Şifreleme iki yönlü olarak yapılırken hashing yalnızca tek yönlüdür.
- Temel amaç herhangi bir dosya veya veri parçasının değiştirilmediğini, üzerinde oynanmadığını doğrulamaktır.
- Ele alınan veri kümesindeki herhangi bir veri değişimi bütün hash'in değişmesine sebep olur.
-

"""

print(hash(input()))
