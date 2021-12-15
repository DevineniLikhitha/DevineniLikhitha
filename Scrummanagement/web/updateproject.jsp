<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ page import="java.sql.*" %>
<%! String driverName = "com.mysql.jdbc.Driver";%>
<%!String url = "jdbc:mysql://localhost:3306/scrumtool";%>
<%!String user = "root";%>
<%!String psw = "null";%>
<%
String projectid = request.getParameter("projectid");
String projectname=request.getParameter("projectname");
String description=request.getParameter("description");

if(projectid != null)
{
Connection con = null;
PreparedStatement ps = null;
int projectID = Integer.parseInt(projectid);
try
{
Class.forName(driverName);
con = DriverManager.getConnection(url,user,psw);
String sql="Update projects set projectid=?,projectname=?,description=? where projectid="+projectid;
ps = con.prepareStatement(sql);
ps.setString(1,projectid);
ps.setString(2, projectname);
ps.setString(3, description);

int i = ps.executeUpdate();
if(i > 0)
{
out.print("Record Updated Successfully");
  
}
else
{
out.print("There is a problem in updating Record.");
}
}
catch(SQLException sql)
{
request.setAttribute("error", sql);
out.println(sql);
}
}
%>