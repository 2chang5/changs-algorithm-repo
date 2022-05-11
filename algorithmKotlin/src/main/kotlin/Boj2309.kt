import java.io.BufferedReader
import java.io.InputStreamReader

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    var list = mutableListOf<Int>()


    for(i in 1..9){
        list.add(br.readLine().toInt())
    }


    fun <T> combination(answer: MutableList<List<T>>, el: List<T>, ck: Array<Boolean>, start: Int, target: Int) {
        if(target == 0) {
            answer.addAll( listOf(el.filterIndexed { index, t -> ck[index] }) )
        } else {
            for(i in start until el.size) {
                ck[i] = true
                combination(answer, el, ck, i + 1, target - 1)
                ck[i] = false
            }
        }
    }
    
}