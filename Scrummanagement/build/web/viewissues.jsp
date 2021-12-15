<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%
String id = request.getParameter("userid");
String driver = "com.mysql.jdbc.Driver";
String connectionUrl = "jdbc:mysql://localhost:3306/";
String database = "scrumtool";
String userid = "root";
String password = "null";
try {
Class.forName(driver);
} catch (ClassNotFoundException e) {
e.printStackTrace();
}
Connection connection = null;
Statement statement = null;
ResultSet resultSet = null;
%>
<!DOCTYPE html>
<html>
    <head> 
    <meta charset = "utf-8">
    <title> view issues</title>
    <meta name="viewport" content ="width=device-width, initial- scale=1.0">
     
    <link rel="stylesheet" href="style.css">
   

    <style>
       
        *{
            padding: 0;
            margin: 0;
            text-decoration: none;
            list-style: none;
           /* text-align: right; */
          }
          body {
              font-family: Arial, Helvetica, sans-serif;
              }
              nav{
                  height: 80px;
                  width: 100%;
                  background: #04B4AE;
              }    
              nav li {
                  
                  display: inline-block;
                  margin:  0 8px;
                  line-height: 80px;
                  
              }
              nav a{
                  color: white;
                  font-size: 18px;
                  
                  
              }
 #issues {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#issues td, #issues th {
  border: 1px solid #ddd;
  padding: 8px;
}

#issues tr:nth-child(even){background-color: #f2f2f2;}

#issues tr:hover {background-color: #ddd;}

#issues th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04B4AE; 
  color: white;
}
/* .button{
              height:55px;
              width:100px;
              margin: 5px;
              background-color: #04B4AE; 
              color: white;
 }*/ 
      .button{font-size: 20px;
         padding:5px;
         border-radius: 5px;
         margin: 5px;
         background-color: #04B4AE;
         color: white;}
    
    </style>
    </head>
<body>
 <nav>
      
        

     <label class = "logo">  </label> 
    <ul>
         <li><a href="Home.html">Home</a></li>
       
        <li><a href="Project1.html">Projects</a></li>
         <li><a href="issues.html">Issues</a></li>
       
        <li><a href="viewissues.jsp">Product Backlog</a></li>
        <li><a href="viewsprintbacklog.jsp">Sprint Backlog</a></li>
        <li><a href="sprint.html">Sprints</a></li>
           <li style="float:right"><a href="Login.html">Logout</a></li>
    
    </ul><br><br>
     <center><h1> List of Issues</h1></center><br><br>
     
<table id="issues">

<tr>
<th style="text-align: center;">Issue Id</th>
<th style="text-align: center;">Issue Name</th>
<th style="text-align: center;">Issue Type</th>
<th style="text-align: center;">Description</th>

<th style="text-align: center;">Status</th>
<th style="text-align: center;">Sprint No</th>
<th style="text-align: center;">Update</th>



</tr>
<%
try{
connection = DriverManager.getConnection(connectionUrl+database, userid, password);
statement=connection.createStatement();
String sql ="select * from issues";
resultSet = statement.executeQuery(sql);
while(resultSet.next()){
%>
<center>
<tr>
<td style = "text-align: center;"><%=resultSet.getString("issueid") %></td>
<td style="text-align: center;"><%=resultSet.getString("issuename") %></td>
<td style="text-align: center;"><%=resultSet.getString("issuetype") %></td>
<td style="text-align: center;"><%=resultSet.getString("issuedescription") %></td>

<td style="text-align: center;"><%=resultSet.getString("status") %></td>
<td style="text-align: center;"><%=resultSet.getString("sprintid") %></td>

<td> <button class="button"> <a href="updateissueform.jsp?issueid=<%=resultSet.getString("issueid")%>">update</a></button></td>
</tr></center>
<%
}
connection.close();
} catch (Exception e) {
e.printStackTrace();
}
%>
</table>
 </nav>
</body>
</html>