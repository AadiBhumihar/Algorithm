public class dfsdemo { 
 public static void main(String agrs[])  {
 	String str = "238164705";
 	String goal = "123456780";
 	
 	DepthFS dfs = new DepthFS(str,goal);
 	dfs.doSearch();
 	
 	}
 	
}
