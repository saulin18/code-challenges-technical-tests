
public class DynamicArr {

    Double length;
    Object[] arr;

    public DynamicArr(Double length) {
        this.length = length;
        this.arr = new Object[length.intValue()];
    }

    public void add(Object item) {
        if (arr.length == length) {
            resize();
        }
        arr[length.intValue()] = item;
        length++;
    }

    public void resize() {
        var newArray = new Object[arr.length * 2];
        for (int i = 0; i < arr.length; i++) {
            newArray[i] = arr[i];
        }
        arr = newArray;
    }

    public void shrink() {
        var newArray = new Object[arr.length / 2];
        for (int i = 0; i < newArray.length; i++) {
            newArray[i] = arr[i];
        }
        arr = newArray;
    }

    public Object get(int index) {
        if (index >= 0 && index < length) {
            return arr[index];
        }
        throw new IndexOutOfBoundsException("Index: " + index + ", Length: " + length);
    }

    public void remove(int index) {
        try {
            var  _ = this.get(index);
        } catch (Exception e) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Length: " + length);
        }

        for (int i = index; i < length - 1; i++) {
            arr[i] = arr[i + 1];
        }
        length--;
        if (length < arr.length / 2) {
            shrink();
        }
    }

    public int size() {
        return length.intValue();
    }

}
