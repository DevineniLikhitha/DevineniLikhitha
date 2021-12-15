<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>

<%
String projectid=request.getParameter("projectid");
String projectname=request.getParameter("projectname");
String description=request.getParameter("description");

try
{
Class.forName("com.mysql.jdbc.Driver");
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/scrumtool", "root", "null");
Statement st=conn.createStatement();

int i=st.executeUpdate("insert into projects(projectid,projectname,description)values('"+projectid+"','"+projectname+"','"+description+"')");
        out.println("Data is successfully inserted!");

        }
catch(Exception e)
{
System.out.print(e);
e.printStackTrace();
}
%>