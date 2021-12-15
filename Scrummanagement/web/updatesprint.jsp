<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ page import="java.sql.*" %>
<%! String driverName = "com.mysql.jdbc.Driver";%>
<%!String url = "jdbc:mysql://localhost:3306/scrumtool";%>
<%!String user = "root";%>
<%!String psw = "null";%>
<%
String sprintid = request.getParameter("sprintid");
String sprintname=request.getParameter("sprintname");

String startdate=request.getParameter("startdate");
String enddate=request.getParameter("enddate");

if(sprintid != null)
{
Connection con = null;
PreparedStatement ps = null;
int sprintID = Integer.parseInt(sprintid);
try
{
Class.forName(driverName);
con = DriverManager.getConnection(url,user,psw);
String sql="Update sprints set sprintid=?,sprintname=?,startdate=?,enddate=? where sprintid="+sprintid;
ps = con.prepareStatement(sql);
ps.setString(1,sprintid);
ps.setString(2, sprintname);

ps.setString(3, startdate);
ps.setString(4, enddate);

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