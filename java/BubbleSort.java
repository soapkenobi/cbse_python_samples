import java.util.Scanner;

class BubbleSort{
	public static void main(String[] args){
		int[] arr = new int[args.length];
		for(int i = 0; i<args.length; i++ )arr[i] = Integer.parseInt(args[i]);
		for(int i = 0; i<arr.length; i++)
			for(int j = 0; j<arr.length-1; j++)
				if(arr[j]>arr[j+1]){
					int temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
		String arrStr = "[";
		for(int i:arr) arrStr += i + (i!=arr[arr.length-1]? ", " :"]");
		System.out.println(arrStr);
	}
}
