https://pep8-ja.readthedocs.io/ja/latest/
> _single_leading_underscore: "内部でだけ使う" ことを示します。 たとえば from M import * は、アンダースコアで始まる名前のオブジェクトをimportしません。
> 
> single_trailing_underscore_: Python のキーワードと衝突するのを避けるために使われる規約です。例を以下に挙げます:
> 
> tkinter.Toplevel(master, class_='ClassName')
> __double_leading_underscore: クラスの属性に名前を付けるときに、名前のマングリング機構を呼び出します (クラス Foobar の __boo という名前は _FooBar__boo になります。以下も参照してください)
> 
> 型変数の名前
> PEP 484 で導入された型変数の名前には、通常 CapWords 方式を使うべきです。また、 T や AnyStr や Num のような短い名前が好ましいです。 共変や反変の振る舞いをする変数を宣言するために _co や _contra のような名前を変数の末尾に付け加えることを推奨します:
> 
> from typing import TypeVar
> 
> VT_co = TypeVar('VT_co', covariant=True)
> KT_contra = TypeVar('KT_contra', contravariant=True)
> 
> Python はアンダースコアが先頭に二つ付いた名前にクラス名を追加します。つまり、クラス Foo に __a という名前の属性があった場合、この名前は Foo.__a ではアクセスできません (どうしてもアクセスしたいユーザーは Foo._Foo__a とすればアクセスできます)。
