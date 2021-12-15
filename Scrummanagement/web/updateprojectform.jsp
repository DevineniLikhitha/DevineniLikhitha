<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%
String projectid = request.getParameter("projectid");
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
<%
try{
connection = DriverManager.getConnection(connectionUrl+database, userid, password);
statement=connection.createStatement();
String sql ="select * from projects where projectid="+projectid;
resultSet = statement.executeQuery(sql);
while(resultSet.next()){
%>
<!DOCTYPE html>
<html>
    <head>
        <style>/*styling from w3 schools-w3schools.com*/
       
        input[type=submit] {
           font-size: 20px;
         padding:5px;
         border-radius: 5px;
         margin: 5px;
         background-color: #04B4AE;
         color: white;
        }
        
        input[type=submit]:hover {
          background-color: #45a049;
        }
        
        div {
          border-radius: 5px;
          background-color: #f2f2f2;
          
        padding: 20px;
        }
        
         form {
    width: 600px;
    padding: 20px;
    margin: auto;
    background: #CACFD2;
    font-size: 20px; }
        </style>
</head>
    
<body>
<h1>Update Project details</h1>
<div>
<form method="post" action="updateproject.jsp">
<input type="hidden" name="projectid" value="<%=resultSet.getString("projectid") %>">
Project ID:<br>
<input type="text" name="projectid" value="<%=resultSet.getString("projectid") %>">
<br> </br> 
Project Name:<br> 
<input type="text" name="projectname" value="<%=resultSet.getString("projectname") %>">
<br> </br> 
Description:<br>
<input type="text" name="description" value="<%=resultSet.getString("description") %>">
<br> </br> 

<br>
<input type="submit" value="submit">
</form>
</div>
<%
}
connection.close();
} catch (Exception e) {
e.printStackTrace();
}
%>
</body>
</html>