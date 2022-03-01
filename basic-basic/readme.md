# База

## Базовая память

```python
>>> a = 5
>>> b = a
>>> a = 10
>>> b 
5
```

Variables in python are actually a pointer. Integer is an immutable data type. So we put a pointer to "5" in "a", then we put the same pointer to "b", so "b" also points to "5". Next, we change "a" to a new memory field that contains the number "10", but the pointer in "b" still points to "5", so when we call "b", we get "5".

Потому переменные в питоне это по сути ссылки. Int это неизменяемый тип данных. Мы кладем в "а" ссылку на число 5,
далее приравниваем имя "b" к "а", таким образом "b" теперь также ссылается на объект в памяти (5). Затем мы присваем "а" новую ссылку на число "10", но в "b" ссылка не изменится. И по адресу цифры "5" ничего не поменялось, там по прежнему стоит цифра "5".

___

```python
>>> a = [1,]
>>> b = a
>>> a.append(10)
>>> b
[1, 10]
```

A list is a mutable object (a list is basically a vector or scalable array). This means that when memory is allocated for the list when "a" is created, in "a" we get a pointer to that memory allocation. And if we somehow change this list, without creating a new one and without copying it, "a" will always remain the same pointer as at the beginning. Next, we place the same pointer on "b". So when we change "a" or "b", we change both of them, because we are changing the object at a specific pointer.

Список это изменяемый объект (также список в питоне это по сути Вектор или расширяемый массив) в питоне, это означает, что когда аллоцируется память для списка, то в "а" кладется ссылка на этот список. Далее мы также передаем эту ссылку в "b". Таким образом, когда мы меняем список с помощью "а", меняется также и список в "b", потому что ссылки обоих имен указывают на одну и ту же память


## Замыкание

A closure is a situation where nested functions use variables/objects that are not specified in its body. Thus, all variables specified in the parent function always remain in memory and are called when the inner function is called. That variables called free variables.
It is supposed that all local variables are collected with GC when function is completed, but "free variables" won't disappear.
