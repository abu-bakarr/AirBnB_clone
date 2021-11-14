class HashTable {
    constructor(size) {
        this.values = {}
        this.size = size
    }

    add(key, value) {
        const hash = genHash(key)

        if (!this.values.hasOwnProperty(hash))
            this.values[hash] = {}
    }

    genHash(data) {
        var dataStr = data.toString()
        var sum = 0;

        for (var i = 0; i < dataStr.length; i++)
            sum += dataStr.charCodeAt(i)
        return sum % this.size
    }
}

(function test() {
    const hashTbl = new HashTable(5)
    console.log(hashTbl.genHash("Lovel"));

})()