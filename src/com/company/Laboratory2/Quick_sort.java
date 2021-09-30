package com.company.Laboratory2;
import java.io.*;
import java.util.*;

public class Quick_sort {
    public static void Merge_sort () {
    }

<<<<<<< HEAD
    public static void main (String args[]) throws Exception{
        Scanner sc = new Scanner(new FileReader(".\\src\\com\\company\\Laboratory2\\sum.txt"));
        PrintStream out = new PrintStream(new File("C:\\Users\\Dell\\IdeaProjects\\Algorithms and Data Structures\\src\\com\\company\\Laboratory2\\sum2.txt"));
        int n;
        n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        Merge_sort(arr, -1, arr.length-1);
        for (int i = 0; i < arr.length; i++){
            out.print(arr[i]+" ");
=======

    public static void main (String args[]) {

        int[] arr = new int[] {10, 4, 8, 7, 6, 1, 9, 3, 2, 5};
        Merge_sort(arr, -1, arr.length-1);
        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
>>>>>>> 2679c319f903ba1870aa6491556fbf097a462bcf
        }
    }
    public static void Merge_sort (int[] arr, int last_lower_number_index, int pivot_element_index) {
        int start_of_section_index = last_lower_number_index;
        int pivot_element = arr[pivot_element_index];
        int pivot_element_index_new = pivot_element_index;
        for (int compared_element_index = start_of_section_index + 1; compared_element_index <= pivot_element_index; compared_element_index++) {
            if (arr[compared_element_index] <= pivot_element) {
                last_lower_number_index += 1;
                if (compared_element_index == pivot_element_index) {
                    pivot_element_index_new = last_lower_number_index;
                }
                int replacement = arr[last_lower_number_index];
                arr[last_lower_number_index] = arr[compared_element_index];
                arr[compared_element_index] = replacement;
            }
        }
        if (start_of_section_index != pivot_element_index_new - 1) {
            Merge_sort(arr, start_of_section_index,
                    pivot_element_index_new - 1);
        }
        if (pivot_element_index_new != pivot_element_index ) {
            Merge_sort(arr, pivot_element_index_new, pivot_element_index);
        }
    }
}
