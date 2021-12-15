/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.*;
import java.sql.*;  
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
/**
 *
 * @author likhi
 */
@WebServlet("/Login")
public class LoginValidate extends HttpServlet {

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
    {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();


        String username = request.getParameter("username");
        String password = request.getParameter("password");
        
        Connection con =null;
        
        try
        {
             Class.forName("com.mysql.jdbc.Driver");
            // System.out.println("Driver Class Loaded");
             con=DriverManager.getConnection("jdbc:mysql://localhost:3306/scrumtool","root","null");
            // System.out.println("Connection Established");
             
             Statement stmt=con.createStatement();
            
             ResultSet rs = stmt.executeQuery(" select  * from users where username='"+username+"' and password='"+password+"' ");
             
             if(rs.next())
             {
                 HttpSession session = request.getSession();
                 
//                 session.setAttribute("uname", username);
//                 session.setAttribute("pwd", password);
             
             
             RequestDispatcher rd = request.getRequestDispatcher("Home.html");
             
             rd.include(request, response);
             
             
             }
             else
             {
                    out.println("Invalid Login details.Try again"); 
             }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }

}

