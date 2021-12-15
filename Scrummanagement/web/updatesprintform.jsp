<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%
String sprintid = request.getParameter("sprintid");
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
String sql ="select * from sprints where sprintid="+sprintid;
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
<h1>Update Sprint details</h1>
<div>
<form method="post" action="updatesprint.jsp">
<input type="hidden" name="sprintid" value="<%=resultSet.getString("sprintid") %>">
<input type="text" name="sprintid" value="<%=resultSet.getString("sprintid") %>">
<br><br>
Sprint Name:<br>
<input type="text" name="sprintname" value="<%=resultSet.getString("sprintname") %>">
<br><br>

Start Date:<br>
<input type="date" name="startdate" value="<%=resultSet.getString("startdate") %>">
<br><br>
End Date:<br>
<input type="date" name="enddate" value="<%=resultSet.getString("enddate") %>">
<br><br>

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