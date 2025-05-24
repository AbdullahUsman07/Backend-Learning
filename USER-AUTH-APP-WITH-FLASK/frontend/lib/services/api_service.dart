import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String _baseUrl = 'http://127.0.0.1:5000';

  // login method

  static Future<Map<String, dynamic>?> login(
    String email,
    String password,
  ) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/login'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'email': email, 'password': password}),
    );
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      return {'token': data['access_token']};
    } else {
      return null;
    }
  }


  // register method
  static Future<Map<String, dynamic>?> regsister(String email, String password, int age,String role) async{
    final response = await http.post(
      Uri.parse('$_baseUrl/register'),
      headers: {'Content-Type':'application/json'},
      body: json.encode({
        'email':email,
        'password':password,
        'age':age,
        'role':role
      }),);

      if(response.statusCode ==201){
        final data = json.decode(response.body);
        return {'token': data['access_token']};
      }else{
        return null;
      }
  }

  // get profile from token
  static Future<Map<String,dynamic>?> getProfile(String token) async{
    final response = await http.get(
      Uri.parse('$_baseUrl/profile'),
      headers:{'Authorization': 'Bearer $token'},
    );

    if(response.statusCode == 200){
      return json.decode(response.body);
    }else{
      return null;
    }
  }
}
