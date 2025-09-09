
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.Stack;
import java.util.Map.Entry;

public  class Main {
    public  static void main(String[] args){
        
        try {
            
            contDup();
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println(e.getMessage());
        }

    }



    private static void mergeSort(int[] nums1 , int m, int[] nums2, int n){
        
        if(n==0){
            System.out.println(nums1);
            return;
        }
        int j=0;
        for(int i=m;i<nums1.length;i++){
            nums1[i] = nums2[j];
            j++;
        }
        Arrays.sort(nums1);

    }

    private static int bestStockSell(int[] arr){
        int bestSell = 0;
        for(int i=0;i<arr.length;i++){
            for (int j = i+1; j < arr.length; j++) {
                if(bestSell < (arr[j] - arr[i])){
                    bestSell=arr[j]-arr[i];
                }
            }
        }
        return bestSell;
    }

    private static StringBuilder findDuplicate(String str){
        StringBuilder sb = new StringBuilder();

        Map<Character,Integer> map = new HashMap<>();
        
        for(char c : str.toCharArray()){
            map.put(c,map.getOrDefault(c, 0)+1);
        }
        map.forEach((k,v) -> {

            if(v > 1) sb.append(k);
        });

        return sb;

    }

    private static void singleNumber(){
        int[] arr = {2,3,1,2,3};
        
        Map<Integer,Integer> map = new HashMap<>();
        
        for(int num : arr){
            map.put(num, map.getOrDefault(num, 0)+1);
        }

        for(Entry<Integer, Integer> mapEntry : map.entrySet()){
            if(mapEntry.getValue()==1){
                System.out.println(mapEntry.getKey());
                return;
            }
        }
    }

    private static void appearsTwice() throws Exception {
        int[] arr = {1,2,2,3,4};
        Set<Integer> set = new HashSet<>();


        for(int num : arr){
            if(!set.add(num)){
                System.out.println(true);
                return;
            }
        }

        
        System.out.println(false);
    }

    private static void contDup(){
        int[] arr = {1,2,3,1,2,1,3};
        int k = 2;
        Map<Integer,Integer> map = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            if (map.containsKey(arr[i])) {
                if (Math.abs(i - map.get(arr[i])) <= k) {
                    System.out.println(i+" "+map.get(arr[i]));
                    System.out.println(true);
                    return;
                }else{
                    map.put(arr[i], i);
                }
            }
            map.put(arr[i], i);
            System.out.println(map);
        }
        
        System.out.println(false);

    }
}
