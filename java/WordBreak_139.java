import java.util.*;

import static java.util.Collections.*;

public class WordBreak_139 {

    public static boolean wordBreak(String s, List<String> wordDict) {
        boolean[] check =new boolean[s.length()+1];
        check[0] =true;
        for(int i =0; i< wordDict.size();i++){
            for(int j = 0; j<){

            }

        }
    }
    public static void main(String[] args){
        String s = "leetcode";
        List<String>wordDict = new ArrayList<>();
        wordDict.add("leet");
        wordDict.add("code");
        wordBreak(s,wordDict);
    }
}
